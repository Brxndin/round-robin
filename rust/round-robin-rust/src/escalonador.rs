use rand::Rng;

use crate::process::Process;
use crate::queue::Queue;

#[derive(Debug)]
pub struct Escalonador {
    quantum: u8,
    ready_queue: Queue,
    block_queue: Queue,
}

impl Escalonador {
    pub fn new(quantum: u8) -> Self {
        Escalonador {
            quantum,
            ready_queue: Queue::new(),
            block_queue: Queue::new(),
        }
    }

    pub fn add_process(&mut self, process: Process) {
        self.ready_queue.enqueue(process);
    }

    pub fn execute(&mut self) -> Result<String, String> {
        let mut rng = rand::rng();

        // todo:
        // verifica se tem Processos na fila
        if self.ready_queue.is_empty() {
            // se nao finaliza e retorna print!("Nao ha processo para executar");
            return Err("Fila de processos vazia!".to_string());
        }

        let mut count = 0;
        // cria loop para executar os processos
        while !self.ready_queue.is_empty() || !self.block_queue.is_empty() {
            println!("Count: {}", count);
            count += 1;
            // dentro do loop:
            // caso tenho satisfeito o tempo do processo apenas da dequeue
            let block_process: bool = rng.random_bool(1.0 / 9.0);

            if !self.block_queue.is_empty() {
                let mut return_processes: Vec<Process> = self.block_queue.decrease();

                while !return_processes.is_empty() {
                    let process = return_processes.remove(0);

                    self.ready_queue.enqueue(process);
                }
            }

            if self.ready_queue.is_empty() {
                println!("oxi vei");
                continue;
            }

            let mut process = self.ready_queue.dequeue();
            println!(
                "{}, {}. id: {}",
                process.process_time, block_process, process.id
            );

            if block_process {
                //println!("processo {} bloqueado!", process.id);
                process.wait_block = 2; // aqui seria o tempo que demora para fazer E/S acho. fixo para
                                        //simplificacoes
                self.block_queue.enqueue(process);
                continue;
            }

            if process.process_time > self.quantum {
                process.process_time -= self.quantum;
                // caso ainda tenha tempo a ser satisfeito retorna ao final da fila (enqueue)
                self.ready_queue.enqueue(process);
                continue;
            }

            //println!("processo {} finalizado!", process.id);
        }

        // nao ha mais itens na fila
        Ok("Exucucao realizada".to_string())
    }
}

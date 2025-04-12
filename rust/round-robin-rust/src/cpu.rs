use crate::process::Process;
use crate::queue::Queue;

#[derive(Debug)]
pub struct Cpu {
    quantum: u8,
    ready_queue: Queue,
}

impl Cpu {
    pub fn new(quantum: u8) -> Self {
        Cpu {
            quantum,
            ready_queue: Queue::new(),
        }
    }

    pub fn add_process(&mut self, process: Process) {
        self.ready_queue.enqueue(process);
    }

    pub fn execute(&mut self) -> Result<String, String> {
        // todo:
        // verifica se tem Processos na fila
        if self.ready_queue.is_empty() {
            // se nao finaliza e retorna print!("Nao ha processo para executar");
            return Err("Fila de processos vazia!".to_string());
        }

        // cria loop para executar os processos
        while !self.ready_queue.is_empty() {
            // dentro do loop:
            // caso tenho satisfeito o tempo do processo apenas da dequeue
            let mut process = self.ready_queue.dequeue();

            if process.process_time > self.quantum {
                process.process_time -= self.quantum;
                // caso ainda tenha tempo a ser satisfeito retorna ao final da fila (enqueue)
                self.ready_queue.enqueue(process);
                continue;
            }

            println!("processo {} finalizado!", process.id);
        }

        // nao ha mais itens na fila
        Ok("Exucucao realizada".to_string())
    }
}

mod escalonador;
mod process;
mod queue;

use crate::escalonador::Escalonador;
use crate::process::Process;
use rand::prelude::*;

fn main() {
    // na real ao invez de Cpu poderia ser Escalonador
    // dai poderia criar ele e ele gerencial o lista dos processos
    // pronto e dos bloqueados
    let mut escalonador = Escalonador::new(5);
    let mut rng = rand::rng();

    let times: [u8; 5] = rng.random();

    println!("Ordem lista:");
    for (index, process_time) in times.iter().enumerate() {
        let process = Process::new(*process_time, index + 1);
        let id = process.id;
        escalonador.add_process(process);
        println!("id {}, tempo {}", id, process_time)
    }
    println!("\n");

    match escalonador.execute() {
        Ok(resp) => println!("{}", resp),
        Err(err) => println!("{}", err),
    }
}

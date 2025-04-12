mod cpu;
mod process;
mod queue;

use crate::cpu::Cpu;
use crate::process::Process;
use rand::prelude::*;

fn main() {
    let mut cpu = Cpu::new(5);
    let mut rng = rand::rng();

    let times: [u8; 5] = rng.random();

    println!("Ordem lista:");
    for (index, process_time) in times.iter().enumerate() {
        let process = Process::new(*process_time, index + 1);
        let id = process.id;
        cpu.add_process(process);
        println!("id {}, tempo {}", id, process_time)
    }
    println!("\n");

    match cpu.execute() {
        Ok(resp) => println!("{}", resp),
        Err(err) => println!("{}", err),
    }
}

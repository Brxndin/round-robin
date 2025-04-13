use crate::process::Process;

#[derive(Debug)]
pub struct Queue {
    pub items: Vec<Process>,
}

impl Queue {
    pub fn new() -> Self {
        Queue { items: Vec::new() }
    }

    pub fn enqueue(&mut self, process: Process) {
        self.items.push(process);
    }

    pub fn dequeue(&mut self) -> Process {
        self.items.remove(0)
    }

    pub fn is_empty(&mut self) -> bool {
        self.items.is_empty()
    }
}

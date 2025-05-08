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

    pub fn decrease(&mut self) -> Vec<Process> {
        let mut vec_return = Vec::new();
        let mut vec_stay = Vec::new();

        for mut process in self.items.drain(..) {
            process.wait_block -= 1;
            if process.wait_block < 1 {
                vec_return.push(process);
            } else {
                vec_stay.push(process);
            }
        }

        self.items = vec_stay;

        vec_return
    }

    pub fn is_empty(&mut self) -> bool {
        self.items.is_empty()
    }
}

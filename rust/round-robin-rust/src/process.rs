#[derive(Debug)]
pub struct Process {
    pub id: usize,
    pub process_time: u8,
}

impl Process {
    pub fn new(process_time: u8, id: usize) -> Self {
        Process { process_time, id }
    }
}

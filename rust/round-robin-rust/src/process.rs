#[derive(Debug)]
pub struct Process {
    pub id: usize,
    pub process_time: u8,
    pub wait_block: u8,
}

impl Process {
    pub fn new(process_time: u8, id: usize) -> Self {
        Process {
            wait_block: 0,
            process_time,
            id,
        }
    }
}

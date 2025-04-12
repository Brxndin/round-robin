Codigo criado para ultilizar o quantum por inteiro em um ciclo da cpu

 if next.process_time < self.quantum {
 se o que precisar pra finalizar, tempo do processo, for menor do que tem disponivel, o
    // quantum, ele faz a subtracao e o resultado subtraido é repassado para o proximo item, isto esta
    // sendo feito para que se tiver 5 processo e cada um ocupa apenas um quantum, ele termina
    // todos os processo em um quantum apenas.

    // OBS da i.a. o "canonico" do round robin nao usa a cpu dessa forma
    // implementada a baixo. ele usar igualmente o quantum para ambos processos
    // da forma implementada abaixo ele usa sempre completamente o quantum
    // no processo canonico do round robin ele nao aproveita por completo o ciclo
    // o que pode gerar quantum restante que era o que estava sendo subtraido do
    // proximo processo para ultilizar completamente o ciclo.
    // nao precisa fazer essa funcao recursiva. :) K K K. mas ele falou que e mais
    // eficiente :)
    // pode ser 0 ou no max o quantum
     let rest_time: u32 = self.quantum - next.process_time;
     self.ready_queue.subtract_next(rest_time);
// }


pub fn subtract_next(&mut self, rest_time: u32) {
        if let Some(mut next) = self.dequeue() {
            // se ainda for maior chama recursivamente
            // rest_time é o tempo de quantum menos o tempo usado pelo cpu
            // sendo o valor restante de ainda reside no ciclo da cpu
            if rest_time > 0 && next.process_time < rest_time {
                self.subtract_next(rest_time - next.process_time)
            }

            // quando nao cai no if quer dizer que usou o tempo total restante do cpu
            // e nao acabou o processo
            // portanto subtrai o resto, tempo que havia sobrado anteriormente
            // e reenfila ele no final pq ele usou o tempo dele no espaco
            next.process_time -= rest_time;
            self.enqueue(next);
        }
    }


// By considering the terms in the Fibonacci sequence whose values do not exceed four million
// , find the sum of the even-valued terms.
struct Fibonacci {
    curr: u64,
    next: u64,
}

impl Iterator for Fibonacci {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        // Get current to return later
        let current = self.curr;

        // Do the thing
        self.curr = self.next;
        self.next += current;

        Some(current)
    }
}

fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 0, next: 1 }
}

fn main() {
    // Problem 1 - Fizz buzz
    let p1: u64 = (1_u64..1000_u64)
        .filter(|&x| x.rem_euclid(3) == 0 || x.rem_euclid(5) == 0)
        .sum();

    println!("Problem 1 answer: {}", p1);
    assert_eq!(233168, p1);

    // Problem 2 - fibonacci
    for x in fibonacci().take(10) {
        println!("{}", x);
    }
    let p2: u64 = fibonacci()
        .filter(|&x| x.rem_euclid(2) == 0)
        .take_while(|&x| x <= 4_000_000_u64)
        .sum();

    println!("Problem 2 answer: {}", p2);
    assert_eq!(4613732, p2);
}

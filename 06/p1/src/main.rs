use std::env;
use std::fs;

fn main() {
    let argv: Vec<String> = env::args().collect();
    if argv.len() != 3 {
        panic!("check args");
    }
    let path = &argv[1];
    let days = &argv[2].parse::<u16>().unwrap();
    let input = match fs::read_to_string(path) {
        Err(err) => panic!("Could not open {}: {}", path, err),
        Ok(file) => file,
    };

    let mut init: Vec<i64> = input
        .trim()
        .split(',')
        .map(|str| str.parse::<i64>().unwrap())
        .collect();

    for day in 1..=*days {
        let temp_init = init.clone();
        for (i, fish) in temp_init.iter().enumerate() {
            let mut new_fish = fish - 1;
            if new_fish < 0 {
                init.push(8);
                new_fish = 6;
            }
            init[i] = new_fish;
        }
        drop(temp_init);
        println!("Day {} with {} fishes", day, &init.len());
    }
    /*
        print!("After {} days: ", *days);
        for fish in &init {
            print!("{}, ", fish);
        }
        print!("\n");
    */
    println!("A total of {} lanternfishes", init.len());
}

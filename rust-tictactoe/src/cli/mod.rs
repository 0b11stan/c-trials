use std::io;
use std::io::Write;
use Player;

pub fn read_name(player_symbol: char) -> String {
    input(format!("Player {} : ", player_symbol).as_ref())
}

pub fn display_winner(player: &Player) {
    println!("{} won, congratulation !!", player.name.to_uppercase());
}

pub fn display_name_conflict_message() {
    println!("Players can't call alike.");
}

pub fn display_cell_conflict_message() {
    println!("This cell is already filled.");
}

pub fn read_move(player: &Player, grid: &[[&Player; 3]; 3]) -> (usize, usize) {
    display_grid(player, grid);

    let row = input("ROW : ");
    let col = input("COL : ");

    (row.parse().unwrap(), col.parse().unwrap())
}

fn display_grid(player: &Player, _grid: &[[&Player; 3]; 3]) {
    println!("Your turn {} ...", player.name);
    println!("   1   2   3");
    for (index, row) in _grid.iter().enumerate() {
        println!("{}  {} | {} | {}", index+1, row[0].symbol, row[1].symbol, row[2].symbol);
    }
}

fn input(message: &str) -> String {
    print!("{}", message);
    io::stdout().flush().unwrap();
    read_line()
}

fn read_line() -> String {
    let mut input = String::new();
    let input_reader = io::stdin().read_line(&mut input);

    match input_reader {
        Ok(_size) => input = input.trim().to_string(),
        Err(error) => panic!("error: {}", error),
    };

    input
}

mod cli;

#[derive(Debug)]
pub struct Player {
    pub name: String,
    pub symbol: char,
}

impl PartialEq for Player {
    fn eq(&self, other: &Player) -> bool {
        self.name == other.name
    }
}

impl Player {
    fn won(&self, _grid: &[[&Player; 3]; 3]) -> bool {
        match grid_to_pattern(&self, _grid) {
            0b111000000 |
            0b000111000 |
            0b000000111 |
            0b100100100 |
            0b010010010 |
            0b001001001 |
            0b100010001 |
            0b001010100 => true,
            _ => false
        }
    }
}

fn grid_to_pattern(player: &Player, _grid: &[[&Player; 3]; 3]) -> i32 {
    let mut output = 0;
    let mut power = 9;

    for row in _grid {
        for cell in row {
            power -= 1;
            if cell == &player { output += 2_i32.pow(power); }
        }
    }

    output
}

fn main() {
    let (x_name, o_name) = read_names_checked();

    let player_x = Player { name: x_name, symbol: 'X' };
    let player_o = Player { name: o_name, symbol: 'O' };
    let empty_player = Player { name: "".parse().unwrap(), symbol: ' ' };

    let mut grid: [[&Player; 3]; 3] = [[&empty_player; 3]; 3];

    let mut current_player = &player_o;
    let mut next_player = &player_x;

    while !current_player.won(&grid) {
        let prev_player = current_player;
        current_player = next_player;
        next_player = prev_player;

        let (row, col) = read_move_checked(current_player, &empty_player, &grid);
        grid[row - 1][col - 1] = current_player;
    };

    cli::display_winner(current_player);
}

fn read_move_checked(current_player: &Player, empty_player: &Player, &grid: &[[&Player; 3]; 3]) -> (usize, usize) {
    loop {
        let (row, col) = cli::read_move(current_player, &grid);
        if grid[row - 1][col - 1] != empty_player { cli::display_cell_conflict_message() } else { return (row, col); }
    }
}

fn read_names_checked() -> (String, String) {
    loop {
        let (x_name, o_name) = (
            cli::read_name('X'),
            cli::read_name('O')
        );
        if o_name == x_name { cli::display_name_conflict_message(); } else { return (x_name, o_name); }
    }
}

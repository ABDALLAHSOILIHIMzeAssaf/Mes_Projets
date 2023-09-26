let currentPlayer = 'X';
let player1Name = '';
let player2Name = '';
let player1Score = 0;
let player2Score = 0;
let board = ['', '', '', '', '', '', '', '', ''];
let gameActive = false;
const winningCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

function startGame() {
    player1Name = document.getElementById('player1Name').value || 'Joueur 1';
    player2Name = document.getElementById('player2Name').value || 'Joueur 2';
    document.getElementById('player1').textContent = player1Name;
    document.getElementById('player2').textContent = player2Name;
    currentPlayer = 'X';
    player1Score = 0;
    player2Score = 0;
    updateScores();
    resetGame();
    gameActive = true;
}

function updateScores() {
    document.getElementById('score1').textContent = player1Score;
    document.getElementById('score2').textContent = player2Score;
}

function checkWinner() {
    for (const combo of winningCombinations) {
        const [a, b, c] = combo;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            gameActive = false;
            return board[a];
        }
    }
    if (!board.includes('')) {
        gameActive = false;
        return 'T';
    }
    return null;
}

function makeMove(cellIndex) {
    if (gameActive && board[cellIndex] === '') {
        board[cellIndex] = currentPlayer;
        document.getElementsByClassName('cell')[cellIndex].textContent = currentPlayer;
        const winner = checkWinner();
        if (winner === 'T') {
            document.getElementById('message').textContent = "Match nul !";
        } else if (winner) {
            document.getElementById('message').textContent = `${winner === 'X' ? player1Name : player2Name} a gagné !`;
            if (winner === 'X') {
                player1Score++;
            } else {
                player2Score++;
            }
            updateScores();
        } else {
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        }
    }
}

function replayGame() {
    if (!gameActive) {
        resetGame();
        gameActive = true;
    }
}

function resetGame() {
    board = ['', '', '', '', '', '', '', '', ''];
    document.getElementById('message').textContent = '';
    const cells = document.getElementsByClassName('cell');
    for (const cell of cells) {
        cell.textContent = '';
    }
    currentPlayer = 'X';
}

document.getElementById('resetBtn').addEventListener('click', startGame);

startGame();

    
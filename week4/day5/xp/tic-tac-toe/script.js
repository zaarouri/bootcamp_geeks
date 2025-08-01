document.addEventListener('DOMContentLoaded', () => {
  // ---- DOM ----
  const diffSel   = document.getElementById('difficulty'); // 'easy' | 'hard'
  const playerSel = document.getElementById('players');    // 'X' | 'O'
  const resetBtn  = document.getElementById('resetButton');
  const statusEl  = document.getElementById('status');
  const boardEl   = document.getElementById('gameBoard');
  const cells     = Array.from(boardEl.querySelectorAll('.cell'));

  // ---- State ----
  let board = Array(9).fill(null); // values: null | 'X' | 'O'
  let human = playerSel.value;     // 'X' or 'O'
  let ai    = human === 'X' ? 'O' : 'X';
  let current = 'X';               // X always starts
  const WINS = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
  ];

  // ---- Rendering ----
  function render() {
    cells.forEach((c, i) => {
      const mark = board[i] ?? '';
      c.dataset.mark = mark;        // drives ::after content
      c.classList.remove('x','o','win');
      if (mark === 'X') c.classList.add('x');
      if (mark === 'O') c.classList.add('o');
    });
  }

  function setStatus(text) {
    statusEl.textContent = text || '';
  }

  // ---- Board helpers ----
  function emptySquares(b = board) {
    const out = [];
    for (let i = 0; i < 9; i++) if (!b[i]) out.push(i);
    return out;
  }

  function winningLine(b = board) {
    for (const line of WINS) {
      const [a,m,n] = line;
      if (b[a] && b[a] === b[m] && b[m] === b[n]) return line;
    }
    return null;
  }

  function checkWinner(b = board) {
    const line = winningLine(b);
    if (line) return b[line[0]]; // 'X' or 'O'
    return emptySquares(b).length === 0 ? 'draw' : null;
  }

  function setMark(i, mark) {
    if (!board[i]) {
      board[i] = mark;
      return true;
    }
    return false;
  }

  function switchTurn() {
    current = current === 'X' ? 'O' : 'X';
  }

  function highlightWin() {
    const line = winningLine();
    if (!line) return;
    line.forEach(i => cells[i].classList.add('win'));
  }

  // ---- AI ----
  function aiMoveEasy() {
    const options = emptySquares();
    if (options.length === 0) return;
    const choice = options[Math.floor(Math.random() * options.length)];
    setMark(choice, ai);
  }

  function scoreOutcome(result, depth) {
    if (result === ai)    return 10 - depth;   // faster win is better
    if (result === human) return depth - 10;   // slower loss is better
    return 0;
  }

  function bestMove(b, player, alpha, beta, depth = 0) {
    const res = checkWinner(b);
    if (res) return { score: scoreOutcome(res, depth), index: -1 };

    let best = { score: player === ai ? -Infinity : Infinity, index: -1 };

    for (const i of emptySquares(b)) {
      b[i] = player;
      const next = bestMove(b, player === 'X' ? 'O' : 'X', alpha, beta, depth + 1);
      b[i] = null;

      if (player === ai) {
        if (next.score > best.score) best = { score: next.score, index: i };
        alpha = Math.max(alpha, next.score);
      } else {
        if (next.score < best.score) best = { score: next.score, index: i };
        beta = Math.min(beta, next.score);
      }
      if (beta <= alpha) break; // prune
    }
    return best;
  }

  function aiMoveHard() {
    const clone = board.slice();
    const { index } = bestMove(clone, ai, -Infinity, Infinity, 0);
    if (index !== -1) setMark(index, ai);
  }

  function aiMove() {
    if (diffSel.value === 'easy') aiMoveEasy();
    else aiMoveHard();
  }

  // ---- Flow ----
  function endIfFinished() {
    const result = checkWinner();
    if (!result) return false;

    if (result === 'draw') {
      setStatus('Draw!');
    } else {
      setStatus(`${result} wins!`);
      highlightWin();
    }
    return true;
  }

  function handleCellClick(e) {
    const t = e.target;
    if (!t.classList.contains('cell')) return;

    const idx = Number(t.id);            // ids are 0..8
    if (Number.isNaN(idx)) return;

    // Ignore if finished
    if (checkWinner()) return;

    // Only human turn is clickable
    if (current !== human) return;

    // Human plays
    if (!setMark(idx, human)) return;    // occupied
    render();
    if (endIfFinished()) return;

    // AI plays
    switchTurn();
    aiMove();
    render();
    if (!endIfFinished()) switchTurn();
  }

  function resetGame() {
    board = Array(9).fill(null);
    human = playerSel.value;
    ai = human === 'X' ? 'O' : 'X';
    current = 'X';
    setStatus('');
    render();
    maybeAiStarts();
  }

  function maybeAiStarts() {
    if (human === 'O' && current === 'X') {
      aiMove();
      render();
      if (!endIfFinished()) switchTurn();
    }
  }

  // ---- Events ----
  boardEl.addEventListener('click', handleCellClick);
  resetBtn.addEventListener('click', resetGame);

  // if player side changes mid-game, reset so turn order stays valid
  playerSel.addEventListener('change', resetGame);

  // difficulty can change on the fly; if you prefer restart, use: diffSel.addEventListener('change', resetGame);
  diffSel.addEventListener('change', () => { /* no reset by default */ });

  // ---- Start ----
  render();
  maybeAiStarts();
});

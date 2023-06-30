const eventSource = new EventSource('');
let PLAY_MODE = "NO_PLAY" // "SINGLE" || "EASY" || "HARD" || "NO_PLAY"

const nodes = [document.getElementById("0 0"),
    document.getElementById("0 1"),
    document.getElementById("0 2"),
    document.getElementById("1 0"),
    document.getElementById("1 1"),
    document.getElementById("1 2"),
    document.getElementById("2 0"),
    document.getElementById("2 1"),
    document.getElementById("2 2")]

const WINNING_COMBINATIONS = [
  // горизонтальные комбинации
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  // вертикальные комбинации
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  // диагональные комбинации
  [0, 4, 8],
  [2, 4, 6]
];

function checkWin(board) {
  for (let combo of WINNING_COMBINATIONS) {
    if (board[combo[0]] === "x" &&
        board[combo[1]] === "x" &&
        board[combo[2]] === "x") {
        alert("X - win")
      return true;
    }
      for (let combo of WINNING_COMBINATIONS) {
    if (board[combo[0]] === "o" &&
        board[combo[1]] === "o" &&
        board[combo[2]] === "o") {
        alert("O - win")
      return true;
    }
  }
  }
  return false;
}

function checkTie(board) {
  let statement = !board.includes("");
  if (statement === true){
      alert("It's a tie")
      return true
  }
  else{
      return false
  }
}

const playButton = document.querySelector(".button")
const modal = document.querySelector(".modal")

let gameSide = undefined
let difficult = undefined;

nodes.forEach(node => {
    node.addEventListener("click", e => {
        if (PLAY_MODE === "SINGLE") {
            const id = e.target.id;
            console.log(id)
            fetch("single/move", {
                method: "POST",
                body: JSON.stringify({id: id}),
            })
        }
    })
})

playButton.addEventListener("click", () => {
    modal.classList.toggle("modal-show")
})
const noBotPlay = document.querySelector("#no-bot")
noBotPlay.addEventListener("click", (e) => {
    fetch("single", {})
    PLAY_MODE = "SINGLE"
    if (modal.classList.contains("modal-show")) modal.classList.remove("modal-show")
})

document.addEventListener('DOMContentLoaded', function () {
    console.log('document was not ready, place code here');
    setInterval(() => {
        fetch("update").then(res => res.json()).then(res => {

            Object.values(res.table).forEach((item, i) => {
                nodes[i].textContent = item;
            })
        })
    }, 500)
});


const ezXBtn = document.querySelector("#ez-x")
const ezOBtn = document.querySelector("#ez-o")

const hardXBtn = document.querySelector("#hard-x")
const hardOBtn = document.querySelector("#hard-o")

ezXBtn.addEventListener("click", (e) => {
    e.preventDefault();
    ezSide("x")
})

ezOBtn.addEventListener("click", (e) => {
    e.preventDefault();
    ezSide("o")
})

hardXBtn.addEventListener("click", (e) => {
    e.preventDefault();
    hardSide("x")
})
hardOBtn.addEventListener("click", (e) => {
    e.preventDefault();
    hardSide("o")
})

nodes.forEach(item => {
    item.addEventListener("click", (e) => {
        if (!gameSide || !difficult) return;

        if (gameSide === "x") {
            if (difficult === "easy") {
                fetch("easy-move", {
                    method: "POST",
                    body: JSON.stringify({side: "x", move: e.target.id})
                })
            }
            if (difficult === "hard") {
                fetch("hard-move", {
                    method: "POST",
                    body: JSON.stringify({side: "x", move: e.target.id})
                })
            }}

                if (gameSide === "o") {
            if (difficult === "easy") {
                fetch("easy-move", {
                    method: "POST",
                    body: JSON.stringify({side: "o", move: e.target.id})
                })
            }
            if (difficult === "hard") {
                fetch("hard-move", {
                    method: "POST",
                    body: JSON.stringify({side: "o", move: e.target.id})
                })
            }}

    })
})

function ezSide(side) {
    fetch("ezbot-side", {
        method: "POST",
        body: JSON.stringify({side})
    })
    modal.classList.toggle("modal-show")
    difficult = "easy"
    gameSide = side
}
function hardSide(side) {
    fetch("hardbot-side", {
        method: "POST",
        body: JSON.stringify({side})
    })
    modal.classList.toggle("modal-show")
    difficult = "hard"
    gameSide = side
}



function showAlert() {
        alert("Событие views.py произошло!");
    }
// src/components/Game.js

import React, { useState, useEffect } from "react";
import { v4 as uuidv4 } from "uuid";
import Grid from "../Grid/Grid";
import { useParams } from "react-router-dom";
import socket from "../../socket";
import { Link } from "react-router-dom";
import "./Game.css";
import Winner from "./Winner";

const Game = () => {
	const [board, setBoard] = useState([
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
	]);
	const [game_id, setGameId] = useState("");
	const [colIndex, setColIndex] = useState(0);
	const [gameOver, setGameOver] = useState(null);
	const [gameStarted, setGameStarted] = useState(false);
	const [trigger, setTrigger] = useState(true);
	const { id } = useParams();
	console.log(id);
	useEffect(() => {
		// Listen for 'connect' event from the server
		socket.on("connect", () => {
			console.log("Connected to server");
		});

		// Listen for 'disconnect' event from the server
		socket.on("disconnect", () => {
			console.log("Disconnected from server");
		});

		if (id === "1" && gameStarted) {
			socket.emit("human_join", {
				game_id: { game_id },
				player: { id },
			});
		} else if (id === "2" && gameStarted) {
			socket.on("update_board", (data) => {
				console.log("board updated" + data.board);
				// Update the board state
				setBoard(data.board);
				if (data.player === 1) {
					socket.emit("ai1_turn", {
						game_id: { game_id },
						player: 2,
					});
				}
			});
		} else if (id === "3" && gameStarted === true) {
			socket.on("update_board", (data) => {
				console.log("board updated" + data.board);
				// Update the board state
				setBoard(data.board);
				if (data.player === 1) {
					socket.emit("ai1_turn", {
						game_id: { game_id },
						player: 1,
					});
				} else if (data.player === 2) {
					socket.emit("ai2_turn", {
						game_id: { game_id },
						player: 2,
					});
				}
			});
		}
		// Listen for 'update_board' event from the server

		//listen for 'invalid_column' event from the server
		socket.on("invalid_column", () => {
			console.log("invalid column");
			setGameOver("Invalid column");
		});

		//listen for winner event from the server
		socket.on("game_over", (data) => {
			console.log(data.winner);
			setGameOver(data.winner);
		});

		// Clean up when the component unmounts
		return () => {
			socket.off("update_board");
		};
	}, [gameStarted, id, game_id, colIndex]);

	// Handle click on a column
	const handleColumnClick = (columnIndex) => {
		// Emit 'human_turn' event to the server
		console.log("column clicked" + columnIndex);
		setColIndex(columnIndex);
		socket.emit("human_turn1", {
			game_id: { game_id },
			column: { columnIndex },
		});
	};

	const startGame = () => {
		// Emit 'start_game' event to the server
		const game_id = uuidv4();
		setGameId(game_id);
		setGameStarted(true);
		console.log("sending start game");
		socket.emit("start_game", { game_id: { game_id } });
		if (id === "3") {
			socket.emit("ai1_turn", {
				game_id: { game_id },
				player: 1,
			});
		}
	};
	return (
		<div className="game-container">
			<div className="navbar">
				<div className="cont">
					<Link to="/" className="nav-bar__button">
						Home
					</Link>
					<Link to="/menu" className="nav-bar__button">
						Menu
					</Link>
					<Link to="/rules" className="nav-bar__button">
						Rules
					</Link>
				</div>
			</div>
			<div className="cont1">
				<h1 className="game-title">Connect Four Game</h1>
				<div className="p" onClick={startGame}>
					Start Game
				</div>
			</div>
			<div className="game">
				{id === "1" && (
					<div className="game">
						<Grid
							className="grid"
							board={board}
							onColumnClick={handleColumnClick}
						/>
						<div className="players">
							<div className="p1">
								{/* <img src="./akatsuki.png" alt="pog" /> */}
								Player 1
							</div>
							<div className="p2">
								{/* <img src="./pog.png" alt="pog" /> */}
								Player 2
							</div>
						</div>
					</div>
				)}
				{id === "2" && (
					<div className="game">
						<Grid
							className="grid"
							board={board}
							onColumnClick={handleColumnClick}
						/>
						<div className="players">
							<div className="p1">
								{/* <img src="./akatsuki.png" alt="pog" /> */}
								Player 1
							</div>
							<div className="p2">
								{/* <img src="./pog.png" alt="pog" /> */}
								AI
							</div>
						</div>
					</div>
				)}
				{id === "3" && (
					<div className="game">
						<Grid className="grid" board={board} onColumnClick={() => {}} />
						<div className="players">
							<div className="p1">
								{/* <img src="./akatsuki.png" alt="pog" /> */}
								AI
							</div>
							<div className="p2">
								{/* <img src="./pog.png" alt="pog" /> */}
								AI
							</div>
						</div>
					</div>
				)}
			</div>
			{/* {gameOver && <h2>{showWinner(gameOver)}</h2>} */}
			{gameOver && (
				<Winner winner={gameOver} trigger={trigger} setTrigger={setTrigger} />
			)}
		</div>
	);
};

export default Game;

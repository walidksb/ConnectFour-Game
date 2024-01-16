// src/components/Game.js

import React, { useState, useEffect, useRef } from "react";
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
	const [winner, setWinner] = useState(null);
	const [gameStarted, setGameStarted] = useState(false);
	const [invalidColumn, setInvalidColumn] = useState(false);
	const [trigger, setTrigger] = useState(true);
	// const [player, setPlayer] = useState(1);
	const { id } = useParams();
	const player = useRef(1);
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
			socket.on("update_board", (data) => {
				console.log("board updated" + data.board);
				// Update the board state
				setBoard(data.board);
				player.current = player.current === 1 ? 2 : 1;
			});
		} else if (id === "2" && gameStarted) {
			socket.on("update_board", (data) => {
				console.log("board updated in player vs ai" + data.board);
				console.log(player);
				// Update the board state
				setBoard(data.board);
				if (data.player === 1) {
					player.current = 2;
					console.log(player.current + "player 2");
					socket.emit("ai1_turn", {
						game_id: { game_id },
						player: player.current,
					});
				} else {
					player.current = 1;
				}
			});
		} else if (id === "3" && gameStarted === true) {
			socket.on("update_board", (data) => {
				console.log("board updated" + data.board);
				// Update the board state
				setBoard(data.board);
				if (data.player === 1) {
					player.current = 2;
					//sleep(2)
					setTimeout(() => {
						socket.emit("ai2_turn", {
							game_id: { game_id },
							player: player.current,
						});
					}, 1000);
				} else if (data.player === 2) {
					player.current = 1;
					setTimeout(() => {
						socket.emit("ai1_turn", {
							game_id: { game_id },
							player: player.current,
						});
					}, 1000);
				}
			});
		}
		// Listen for 'update_board' event from the server

		//listen for 'invalid_column' event from the server
		socket.on("invalid_column", () => {
			console.log("invalid column");
			setInvalidColumn(true);
		});

		//listen for winner event from the server
		socket.on("game_over", (data) => {
			console.log(data.winner);
			setWinner(data.winner);
			setGameOver(true);
		});

		// Clean up when the component unmounts
		return () => {
			socket.off("update_board");
		};
	}, [id, game_id, colIndex]);

	// Handle click on a column
	const handleColumnClick = (columnIndex) => {
		// Emit 'human_turn' event to the server
		console.log("column clicked" + columnIndex);
		setColIndex(columnIndex);
		console.log(player);
		socket.emit("human_turn1", {
			game_id: { game_id },
			column: { columnIndex },
			player: player.current,
		});
		if (invalidColumn) {
			setInvalidColumn(false);
		}
	};

	const startGame = () => {
		// Emit 'start_game' event to the server
		const game_id = uuidv4();
		setGameId(game_id);
		setGameStarted(true);
		// setGameOver(null);
		console.log("sending start game");
		socket.emit("start_game", { game_id: { game_id } });
		//if its AI vs AI (id ==3)  the game satrts automatically and AI1 starts
		if (id === "3") {
			socket.emit("ai1_turn", {
				game_id: { game_id },
				player: player.current,
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
				<div className="start-button" onClick={startGame}>
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
							<h1>VS</h1>
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
							<h1>VS</h1>
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
							<h1>VS</h1>
							<div className="p2">
								{/* <img src="./pog.png" alt="pog" /> */}
								AI
							</div>
						</div>
					</div>
				)}
			</div>
			<div className="invalid">{invalidColumn && <h2>Invalid Column</h2>}</div>
			{/* {gameOver && <h2>{showWinner(gameOver)}</h2>} */}
			{gameOver && (
				<Winner winner={winner} trigger={trigger} setTrigger={setTrigger} />
			)}
		</div>
	);
};

export default Game;

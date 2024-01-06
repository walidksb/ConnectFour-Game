import React from "react";
import { Link } from "react-router-dom";
import "./Rules.css";

const Rules = () => {
	return (
		<div className="rules__container">
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
			<div className="rules__content">
				<h1 className="title">RULES</h1>
				<div className="desc1-cont">
					<div className="desc1">
						<img src="./fire.png" alt="fire" />
						<h2 className="description1">OBJECTIVE</h2>
					</div>
					<p>
						Be the first player to connect 4 of the same colored discs in a row
						(either vertically, horizontally, or diagonally).
					</p>
				</div>
				<div className="desc1-cont">
					<div className="desc1">
						<img src="./fire.png" alt="fire" />
						<h2 className="description1">HOW TO PLAY</h2>
					</div>
					<ol>
						<li> 1. Red goes first in the first game.</li>
						<li>
							{" "}
							2. Players must alternate turns, and only one disc can be dropped
							in each turn.
						</li>
						<li>
							{" "}
							3. The game ends when there is a 4-in-a-row or a stalemate.
						</li>
						<li>
							{" "}
							4. The starter of the previous game goes second on the next game.
						</li>
					</ol>
				</div>
			</div>
		</div>
	);
};

export default Rules;

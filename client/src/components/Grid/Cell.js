// src/components/Cell.js

import React from "react";
import "./Cell.css";

const Cell = ({ value, onClick }) => {
	return (
		<div className="cell-container">
			<div
				className={`grid-cell ${
					value === 1 ? "player1" : value === 2 ? "player2" : ""
				}`}
				onClick={onClick}
			>
				{value !== 0 && (
					<div className={`player-piece player${value}`}>{value}</div>
				)}
			</div>
		</div>
	);
};

export default Cell;

// src/components/Grid.js

import React from "react";
import Cell from "./Cell";
import "./Grid.css";

const Grid = ({ board, onColumnClick }) => {
	return (
		<div className="grid_container">
			{board.map((row, rowIndex) => (
				<div key={rowIndex} className="grid_row">
					{row.map((cell, colIndex) => (
						<Cell
							key={colIndex}
							value={cell}
							onClick={() => onColumnClick(colIndex)}
						/>
					))}
				</div>
			))}
		</div>
	);
};

export default Grid;

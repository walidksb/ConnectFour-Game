import React from "react";
import "./Winner.css";
const Winner = (props) => {
	return props.trigger ? (
		<div className="popup">
			<div className="popup-inner">
				{props.winner === 1 && (
					<div className="div">
						<h1 className="winner-title">Congratulations !!!!</h1>
						<h1 className="winner-title">Player 1 WON !!!</h1>
						<img src="/congrats.png" alt="pic" />
					</div>
				)}
				{props.winner === 2 && (
					<div className="div">
						<h1 className="winner-title">Congratulations !!!!</h1>
						<h1 className="winner-title">Player 2 WON !!!</h1>
						<img src="/congrats.png" alt="pic" />
					</div>
				)}
				{props.winner === 0 && <h1 className="winner-title">Its A Tie !!!</h1>}
				{/* <img src="/congrats.png" alt="pic" /> */}
				<div onClick={() => props.setTrigger(false)} className="close-button">
					Close
				</div>
			</div>
		</div>
	) : (
		""
	);
};

export default Winner;

import React from "react";
import "./Winner.css";
const Winner = (props) => {
	return props.trigger ? (
		<div className="popup">
			<div className="popup-inner">
				<h1 className="winner-title">Congratulations !!!!</h1>
				<h1 className="winner-title">Player {props.winner} WON !!!</h1>
				<img src="/congrats.png" alt="pic" />
				<div onClick={() => props.setTrigger(false)} className="close-button">
					Close
				</div>
			</div>
			{/* <div className="navbar">
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
			</div> */}
		</div>
	) : (
		""
	);
};

export default Winner;

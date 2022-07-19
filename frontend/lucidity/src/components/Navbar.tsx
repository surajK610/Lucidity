import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

type NavbarProp = {
  backgroundColor: string;
  user: User | null;
  logOut: () => void;
};

let Navbar = ({ backgroundColor, user, logOut }: NavbarProp) => {
  return (
    <div className="navbar" style={{ backgroundColor: backgroundColor }}>
      <Link to="/" className="link">
        Lucidity
      </Link>
      <Link to="/wrapped" className="link">
        Statistics
      </Link>
      {/* <Link to="/" className="link">
        About
      </Link> */}
      {user ? (
        <>
          <div className="link-right">{user.name}</div>
          <div className="link link-right log-out" onClick={logOut}>
            Log Out
          </div>
        </>
      ) : (
        <Link to="login" className="link link-right">
          Log In
        </Link>
      )}
    </div>
  );
};

export default Navbar;

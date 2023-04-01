import React from 'react';
import './Navbar.css';

interface NavbarProps {}

const Navbar: React.FC<NavbarProps> = () => {
  return (
    <nav className="navbar">
      <div className="navbar__left">
        <a href="/dashboard" className="navbar__item">
          Dashboard
        </a>
        <a href="/miners" className="navbar__item">
          Miners
        </a>
        <a href="/editor" className="navbar__item">
          Editor
        </a>
      </div>
      <div className="navbar__right">
        <div className="user-icon">
          U
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
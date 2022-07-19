import React, { useState } from "react";
import Navbar from "./Navbar";
import "./Emoji.css";

type EmojiUser = {
  name: string;
  rate: number;
  emojis: string;
};

type EmojiProps = {
  mostUsedEmojis: string;
  users: EmojiUser[];
};

const maxStringLength: number = 50;

let Emoji = ({ mostUsedEmojis, users }: EmojiProps) => {
  return (
    <div className="container-emoji">
      <div className="text-container">
        <h1 className="response__average">Emoji Expression!</h1>
        <div className="response__compare">
          Your most used emojis are{" "}
          <span className="color--accent-emoji">{mostUsedEmojis}</span>.
        </div>
      </div>
      <div className="users-container-emoji">
        <h1 className="users__title-emoji">
          Here's who you used emojis with the most:
        </h1>
        <div className="users-grid">
          <div className="user__row__emoji">
            <div></div>
            <div className="grid__header">User</div>
            <div className="grid__header">Emojis Per Day</div>
            <div className="grid__header">Most Used Emojis</div>
          </div>
          {users.map((user, index) => {
            return (
              <div key={index} className="user__row__emoji">
                <div>{index + 1}</div>
                <div>{user.name.substring(0, maxStringLength)}</div>
                <div>{user.rate}</div>
                <div>{user.emojis}</div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default Emoji;

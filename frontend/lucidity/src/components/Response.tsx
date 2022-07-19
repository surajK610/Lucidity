import React, { useState } from "react";
import Navbar from "./Navbar";
import "./Response.css";

type ResponseUser = {
  name: string;
  responseTime: string;
};
type ResponseProps = {
  avgResponseTime: string;
  responseUsers: ResponseUser[];
};

const maxStringLength: number = 50;

let Response = ({ avgResponseTime, responseUsers }: ResponseProps) => {
  return (
    <div className="container">
      <div className="text-container">
        <h1 className="response__average">Your Average Response Time is: </h1>
        <h1 className="response__time color--accent"> {avgResponseTime}</h1>
        <div className="response__compare">
          That's faster than <span className="color--accent">99%</span> of other
          users in the United States.
        </div>
      </div>
      <div className="users-container">
        <h1 className="users__title">
          You responded fastest to the following users:
        </h1>
        <div className="users-grid">
          <div className="user__row">
            <div></div>
            <div className="grid__header">User</div>
            <div className="grid__header">Avg. Resonse Time</div>
          </div>
          {responseUsers.map((user, index) => {
            return (
              <div key={index} className="user__row">
                <div>{index + 1}</div>
                <div style={{ textOverflow: "ellipsis" }}>
                  {user.name.substring(0, maxStringLength)}
                </div>
                <div>{user.responseTime}</div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default Response;

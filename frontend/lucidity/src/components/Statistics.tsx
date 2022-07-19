import React, { useState } from "react";
import Navbar from "./Navbar";
import "./Statistics.css";

type StatisticsProp = {
  averageTextLength: number;
  totalMessages: number;
  convoInitFreq: string;
  msgSentiment: string;
};

let Statistics = ({
  averageTextLength,
  totalMessages,
  convoInitFreq,
  msgSentiment,
}: StatisticsProp) => {
  return (
    <div className="container-big">
      <h2 className="header-statistics">Dive into Summary Statistics!</h2>
      <div className="container-statistics">
        <div className="form-container-statistics">
          <h3 className="form__title-statistics">Total Messages Sent: </h3>
          <h3 className="statistic">
            {totalMessages}{" "}
            <span className="form__title-statistics">messages</span>
          </h3>
        </div>
        <div className="form-container-statistics">
          <h3 className="form__title-statistics">Average Text Length: </h3>
          <h3 className="statistic">
            {averageTextLength}{" "}
            <span className="form__title-statistics">words</span>
          </h3>
        </div>
        <div className="form-container-statistics">
          <h3 className="form__title-statistics">
            Conversation Initiation Frequency:{" "}
          </h3>
          <h3 className="statistic">
            {convoInitFreq} <span className="form__title-statistics"></span>
          </h3>
        </div>
        <div className="form-container-statistics">
          <h3 className="form__title-statistics">Message Sentiment: </h3>
          <h3 className="statistic">
            {msgSentiment}
            <span className="form__title-statistics"> positive</span>
          </h3>
        </div>
      </div>
    </div>
    // Need instructions on how to get the file
  );
};

export default Statistics;

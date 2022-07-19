import React, { useState } from "react";
import Navbar from "./Navbar";
import "./CelebrityComparison.css";
import CelebrityBox from "./CelebrityBox";

type Celebrity = {
  name: string;
  matchPercent: string;
  imgPath: string;
};

type CelebrityComparisonProp = {
  celebrities: Celebrity[];
};

let CelebrityComparison = ({ celebrities }: CelebrityComparisonProp) => {
  return (
    <div className="container-celeb">
      <div className="text-container">
        <h1 className="celebrity_comparison">Celebrity Comparison</h1>
        <div className="celebrity_comp_description">
          Your texting behavior was most similar to these celebrities.
        </div>
      </div>
      <div>
        {celebrities.map((celeb, index) => {
          return (
            <div style={{ padding: "1vh 0" }}>
              <CelebrityBox
                name={celeb.name}
                matchPercent={celeb.matchPercent}
                imgPath="face.jpg"
              ></CelebrityBox>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default CelebrityComparison;

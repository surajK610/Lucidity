import React, { useState } from "react";
import Navbar from "./Navbar";
import "./Personality.css";

interface PersonalityInput {
  personality: string;
}

function Personality(props: PersonalityInput) {
  return (
    <div className="personalityDiv">
      <div className="persTitleDiv">
        <h3 className="persH3">Your Personality While Texting:</h3>
        <h4 className="instructions">
          The Meyers Briggs Personality Indicator classifies your personality
          based on the following concepts: Introversion/Extroversion,
          Sensing/Intuition, Thinking/Feeling, and Judging/Perceiving. Based on
          your text messages, we predicted the following personality type for
          you:
        </h4>
      </div>
      <div className ="userPers">
        <h2 className="persH2">{props.personality}</h2>
      </div>
      <div className="row">
        <div className="col">
          {props.personality.includes("I") ? (
            <div>
              <h1>I</h1>
              <h3>Introverted</h3>
              <p>
                You are "inward-turning" and tend to be thought-oriented, enjoy
                deep and meaningful social interactions, and feel recharged
                after spending time alone
              </p>
            </div>
          ) : (
            <div>
              <h1>E</h1>
              <h3>Extroverted</h3>
              <p>
                You are "outward-turning" and tend to be action-oriented, enjoy
                more frequent social interaction, and feel energized after
                spending time with other people
              </p>
            </div>
          )}
        </div>
        <div className="col">
          {props.personality.includes("N") ? (
            <div>
              <h1>N</h1>
              <h3>Intuition</h3>
              <p>
                You pay more attention to things like patterns and impressions.
                You enjoy thinking about possibilities, imagining the future,
                and abstract theories.
              </p>
            </div>
          ) : (
            <div>
              <h1>S</h1>
              <h3>Sensing</h3>
              <p>
                You tend to pay a great deal of attention to reality,
                particularly to what you can learn from you own senses. You tend
                to focus on facts and details and enjoy getting hands-on
                experience.
              </p>
            </div>
          )}
        </div>
        <div className="col">
          {props.personality.includes("T") ? (
            <div>
              <h1>T</h1>
              <h3>Thinking</h3>
              <p>
                When you make a decision, you like to find the basic truth or
                principle to be applied, regardless of the specific situation
                involved.
              </p>
            </div>
          ) : (
            <div>
              <h1>F</h1>
              <h3>Feeling</h3>
              <p>
                You believe you can make the best decisions by weighing what
                people care about and the points-of-view of persons involved in
                a situation.
              </p>
            </div>
          )}
        </div>
        <div className="col">
          {props.personality.includes("J") ? (
            <div>
              <h1>J</h1>
              <h3>Judging</h3>
              <p>
                You use your decision-making (Judging) preference (whether it is
                Thinking or Feeling) in your outer life.
              </p>
            </div>
          ) : (
            <div>
              <h1>P</h1>
              <h3>Perceiving</h3>
              <p>
                You use your perceiving function (whether it is Sensing or
                Intuition) in your outer life.
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Personality;

import axios from "axios";
import React, { useState, useEffect } from "react";
import "./Login.css";
import { useNavigate } from "react-router-dom";
import Modal from "react-modal";

Modal.setAppElement("#root");

type errorMessage = {
  name: string;
  message: string;
};

type LoginProp = {
  setUser: React.Dispatch<React.SetStateAction<User | null>>;
};

const modalStyle = {
  content: {
    top: "50%",
    left: "50%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)",
    width: "min(90%, 500px)",
    borderRadius: "15px",
  },
  overlay: {
    backgroundColor: "rgba(0, 0, 0, 0.8)",
  },
};

const Login = ({ setUser }: LoginProp) => {
  const navigate = useNavigate();

  const [errorMessages, setErrorMessages] = useState<errorMessage>({
    name: "",
    message: "",
  });
  const [firstTimeUser, setFirstTimeUser] = useState<boolean>(false);

  const [formEmail, setFormEmail] = useState<string>("");
  const [formName, setFormName] = useState<string>("");
  const [formPassword, setFormPassword] = useState<string>("");
  const [modalOpen, setModalOpen] = useState<boolean>(false);

  const renderErrorMessage = (name: string) => {
    return (
      name === errorMessages.name && (
        <div className="error">{errorMessages.message}</div>
      )
    );
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    if (firstTimeUser) {
      const body = {
        name: formName,
        email: formEmail,
        password: formPassword,
      };

      axios({
        method: "POST",
        url: "/user",
        data: body,
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          const user: User = response.data as User;
          setUser(user);
          navigate("../upload", { replace: true });
          console.log(user);
        })
        .catch((error) => {
          if (error.response) {
            console.error(error);
          }
        });
    } else {
      const body = {
        email: formEmail,
        password: formPassword,
      };

      axios({
        method: "POST",
        url: "/user/login",
        data: body,
      })
        .then((response) => {
          const user: User = response.data as User;
          setUser(user);
          navigate("../upload", { replace: true });
          console.log(user);
        })
        .catch((error) => {
          console.error(error);
        });
    }

    e.preventDefault();
  };

  return (
    <div className="login-container">
      <div className="login__left-container">
        <h1 className="login__title">Lucidity</h1>
        <h1 className="login__subtitle">
          The premier AI powered text message analysis platform. 
          <br />
          <br />
          Lucidity uses cutting-edge Data Science algorithms and Machine
          Learning models to help you better understand your texting behavior.{" "}
          <br />
          <br />
          To get started, log in and upload your Facebook Messenger data. Don't worry,
          Lucdity never shares your data and will delete it once you view your results!
        </h1>
      </div>
      <div className="login__right-container">
        <div className="form-container">
          <div className="form__title">
            {firstTimeUser ? "Create an Account" : "Log in to Lucidity"}
          </div>
          <form onSubmit={handleSubmit}>
            <div className="form-row">
              <input
                type="text"
                name="email"
                placeholder="Email"
                required
                value={formEmail}
                onChange={(e) => setFormEmail(e.target.value)}
              />
              {firstTimeUser && (
                <>
                  <input
                    type="text"
                    name="name"
                    placeholder="Name"
                    required
                    value={formName}
                    onChange={(e) => setFormName(e.target.value)}
                  />
                  {renderErrorMessage("uname")}
                </>
              )}
            </div>
            <input
              type="password"
              name="pass"
              placeholder="Password"
              required
              value={formPassword}
              onChange={(e) => setFormPassword(e.target.value)}
            />
            {renderErrorMessage("pass")}
            <input type="submit" />
          </form>
          <div className="form-links">
            <button
              className="form-link"
              onClick={() => setFirstTimeUser((current) => !current)}
            >
              {firstTimeUser ? "Log In" : "New to Lucidity?"}
            </button>
            <button className="form-link">Forgot Password?</button>
          </div>
        </div>
        <div className="terms-box">
          By creating a Lucidity account, you are agreeing to our{" "}
          <span onClick={() => setModalOpen(true)} className="terms-link">
            Terms and Conditions
          </span>
          .
        </div>
      </div>
      <Modal
        isOpen={modalOpen}
        onRequestClose={() => setModalOpen(false)}
        style={modalStyle}
        contentLabel="Terms and Conditions"
      >
        <div className="terms__exit" onClick={() => setModalOpen(false)}>
          &#10005;
        </div>
        <h1 className="terms__title">Terms and Conditions</h1>
        <p>
          We reserve the right to change, modify or remove the content or the
          services from time to time. We cannot guarantee that the Service will
          be available at all times. After submission, your data will not be
          used for any thing other than performing your requested analysis.
          Subsequently it will be immediately deleted. We will retain the
          results of your requested analysis so we can show you again if you
          choose to visit the website. By submitting your data, you consent to
          these terms and conditions.
        </p>
      </Modal>
    </div>
  );
};

export default Login;

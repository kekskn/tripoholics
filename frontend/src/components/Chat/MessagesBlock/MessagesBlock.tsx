import React, { useState, useRef, useEffect } from "react";
import Avatar from "../Avatar/Avatar";
import MessageInputBlock from "../MessageInputBlock/MessageInputBlock";
import MessageItem from "../MessageItem/MessageItem";
import "./MessagesBlock.scss";

import searchImg from "../../../../static/photos/icons/search.png";
import optionsImg from "../../../../static/photos/icons/options.png";

const initialMessages = [
  // "Привет!",
  // "Добрый день",
  // "Как дела?",
  // "Нормально, а у тебя?",
  // "И у меня",
  {
    message: "Привет!",
    author: "Serpuhovskiy",
  },
  {
    message: "Привет)",
    author: "admin",
  },
  {
    message: "Как дела?",
    author: "Serpuhovskiy",
  },
  {
    message: "Отлично, а у тебя?",
    author: "admin",
  },
  {
    message: "Привет!",
    author: "Serpuhovskiy",
  },
  {
    message: "Привет)",
    author: "admin",
  },
  {
    message: "Как дела?",
    author: "Serpuhovskiy",
  },
  {
    message: "Отлично, а у тебя?",
    author: "admin",
  },
  {
    message: "Как дела?",
    author: "Serpuhovskiy",
  },
  {
    message: "Отлично, а у тебя?",
    author: "admin",
  },
  {
    message: "Привет!",
    author: "Serpuhovskiy",
  },
  {
    message: "Привет)",
    author: "admin",
  },
  {
    message: "Как дела?",
    author: "Serpuhovskiy",
  },
  {
    message: "Отлично, а у тебя?",
    author: "admin",
  },
  {
    message: "Как дела?",
    author: "Serpuhovskiy",
  },
  {
    message: "Отлично, а у тебя?",
    author: "admin",
  },
  {
    message: "Привет!",
    author: "Serpuhovskiy",
  },
  {
    message: "Привет)",
    author: "admin",
  },
  {
    message: "Как дела?",
    author: "Serpuhovskiy",
  },
  {
    message: "Отлично, а у тебя?",
    author: "admin",
  },
];

export default function MessagesBlock() {
  const [inputBlockHeight, setInputBlockHeight] = useState("");
  const [messages, setMessages] = useState(initialMessages);
  const messagesBlockRef = useRef<any>();
  const onChangeHeight = (height) => {
    setInputBlockHeight(`${height}px`);
  };

  useEffect(() => {
    const roomName = JSON.parse(
      document.getElementById("room-name").textContent
    );

    const chatSocket = new WebSocket(
      "ws://" + window.location.host + "/ws/my_messages/" + roomName + "/"
    );

    chatSocket.onmessage = function (e) {
      const data = JSON.parse(e.data);
      console.log("data from socket", data);
      setMessages((oldArray) => [
        ...oldArray,
        { message: data.message, author: data.author },
      ]);
      console.log("NEW MESSAGE: ", data.message);
    };

    chatSocket.onclose = function (e) {
      console.error("Chat socket closed unexpectedly");
    };

    document
      .querySelector(".message-input__btn.send-btn")
      ?.addEventListener("click", () => {
        console.log("clicked send");
        const currentUser = document
          .querySelector("#user-name")
          .innerHTML.replace(/[\"]/g, "");
        const messageInputDom = document.querySelector(
          ".message-input"
        ) as HTMLInputElement;
        const message = messageInputDom.value;
        chatSocket.send(
          JSON.stringify({
            message: message,
            author: currentUser,
          })
        );
      });
  }, []);

  useEffect(() => {
    if (messagesBlockRef.current) {
      messagesBlockRef.current.scrollTo(
        0,
        messagesBlockRef.current.scrollHeight
      );
    }
  }, [messages]);

  useEffect(() => {
    setMessages(initialMessages);
  }, [initialMessages]);

  useEffect(() => {
    console.log("CHANGED");
  }, [messages]);

  function renderMessages() {
    const currentUser = document
      .querySelector("#user-name")
      .innerHTML.replace(/[\"]/g, "");
    console.log("currentUser", currentUser);
    return messages.map((item, index) => (
      <MessageItem
        text={item.message}
        isMy={item.author === currentUser}
        isOnline={false}
        isRead
        key={index}
      />
    ));
  }

  console.log("STATE: ", messages);
  return (
    <div className="chat__main-block">
      <div className="chat__messages-block-header">
        <div className="chat__interlocutor">
          <Avatar width={40} height={40} isOnline={false} />
          <div className="chat__interlocutor-info">
            <div className="chat__interlocutor-fullname">Тест Тестов</div>
            <div className="chat__interlocutor-isonline">Онлайн</div>
          </div>
        </div>
        <div className="chat__options">
          <button className="chat__options-block options-search">
            <img src={searchImg} alt="" className="chat__options-search-img" />
          </button>
          <button className="chat__options-block options-options">
            <img
              src={optionsImg}
              alt=""
              className="chat__options-options-img"
            />
          </button>
        </div>
      </div>
      <div className="chat__main-block-wrapper">
        <div
          className="chat__messages-block"
          // style={{ bottom: inputBlockHeight }}
          ref={messagesBlockRef}
        >
          {renderMessages()}
        </div>
      </div>
      <div className="chat__input-block">
        <MessageInputBlock onChangeHeight={onChangeHeight} />
      </div>
    </div>
  );
}

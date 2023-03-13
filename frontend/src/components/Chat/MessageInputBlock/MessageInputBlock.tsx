import React, { useEffect, useRef, useState } from "react";
import data from "@emoji-mart/data";

import smileIcon from "../../../../static/photos/icons/smile.png";
import addFileIcon from "../../../../static/photos/icons/paperclip.png";
import sendIcon from "../../../../static/photos/icons/send.png";
import microIcon from "../../../../static/photos/icons/microphone.png";

import "./MessageInputBlock.scss";
import blockHeightCalc from "../../../utils/blockHeightCalc";

export default function MessageInputBlock({ onChangeHeight }) {
  const [inputValue, setInputValue] = useState("");
  const [isWrittenMessage, setIsWrittenMessage] = useState(false);
  const input = useRef();

  const onInputChange = (e) => {
    if (e.target.value && !isWrittenMessage) setIsWrittenMessage(true);
    if (!e.target.value) setIsWrittenMessage(false);
    setInputValue(e.target.value);
  };

  useEffect(() => {
    onChangeHeight(blockHeightCalc(".chat__input-block"));
    // input.current.addEventListener("keypress", function (e) {
    //   // если пользователь нажал на Enter, выполняем нужный код
    //   // e.preventDefault() для того чтобы отключить действие браузера по умолчанию (обычно это отправка формы).
    //   if (e.which === 13) {
    //     e.preventDefault();
    //     alert("You clicked Enter");
    //   }
    // });
  }, []);

  const onKeyDown = (e) => {
    if (e.which === 13) {
      e.preventDefault();
      // alert("You clicked Enter");
      setInputValue("");
      document.dispatchEvent(new Event("onSendMessage"));
    }
  };

  const onSendMessage = () => {
    console.log("onSendMessage");
    setInputValue("");
    document.dispatchEvent(new Event("onSendMessage"));
  };

  return (
    <div className="message-input-block">
      <div className="message-input-block__field">
        <div className="message-input__left-btns">
          <button className="message-input__btn smile-btn">
            <img src={smileIcon} alt="" />
          </button>
          <button className="message-input__btn file-btn">
            <img src={addFileIcon} alt="" />
          </button>
        </div>
        <input
          // ref={input}
          onKeyDown={onKeyDown}
          className="message-input"
          type="text"
          placeholder="Напишите сообщение..."
          value={inputValue}
          onChange={onInputChange}
        />
        <div className="message-input__right-btns">
          <button
            className="message-input__btn send-btn"
            onClick={onSendMessage}
          >
            <img src={sendIcon} alt="" />
          </button>
        </div>
      </div>
    </div>
  );
}

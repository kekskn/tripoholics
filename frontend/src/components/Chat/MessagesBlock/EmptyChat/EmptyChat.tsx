import React from "react";

import "./EmptyChat.scss";
import emptyChat from "../../../../../static/empty-chat.png";

export default function EmptyChat() {
  return (
    <div className="empty-chat">
      <div className="empty-chat__icon">
        <img src={emptyChat} alt="" className="empty-chat__icon-img" />
      </div>
      <div className="empty-chat__descr">Выберите диалог из списка</div>
    </div>
  );
}

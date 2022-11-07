import React from "react";
import cn from "classnames";

import Avatar from "../Avatar/Avatar";

import "./MessageItem.scss";
import MessageText from "./MessageText";

export default function MessageItem({ isMy, isOnline, isRead }) {
  return (
    <div className={cn("message-item", { my: isMy })}>
      <div className="message-item__avatar">
        <Avatar height={40} width={40} isOnline={isOnline} />
      </div>
      <div className="message-item__info">
        {/* <div className={cn("message-item__text", { read: isRead })}>
          Привет, как дела? Что делаешь?
        </div> */}
        <MessageText isRead={isRead} />
        <MessageText isRead={isRead} />
        <div className="message-item__date">12:37</div>
      </div>
    </div>
  );
}

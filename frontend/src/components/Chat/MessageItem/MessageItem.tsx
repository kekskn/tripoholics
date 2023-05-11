import React from "react";
import cn from "classnames";
import { format, toDate, parseISO } from "date-fns";

import Avatar from "../Avatar/Avatar";
import MessageText from "./MessageText";

import "./MessageItem.scss";

interface IMessageItem {
  isMy: boolean;
  isOnline: boolean;
  isRead: boolean;
  text: string;
  author: string;
  date: string;
  isWithAvatar: boolean;
  isFirst: boolean;
}

export default function MessageItem({
  isMy,
  isOnline,
  isRead,
  text,
  author,
  date,
  isWithAvatar,
  isFirst,
}: IMessageItem) {
  return (
    <div
      className={cn("message-item", { my: isMy, isWithAvatar: isWithAvatar, first: isFirst })}
    >
      {isWithAvatar && (
        <div className="message-item__avatar">
          <Avatar
            height={40}
            width={40}
            isOnline={isOnline}
            letter={author[0]}
          />
        </div>
      )}
      <div className="message-item__info">
        <div className="message-item__main-block">
          {text}
          <div className="message-item__date">
            {format(parseISO(date), "HH:mm")}
          </div>
        </div>
      </div>
    </div>
  );
}

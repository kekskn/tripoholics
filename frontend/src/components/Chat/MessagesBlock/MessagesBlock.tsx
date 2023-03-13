import React, { useState, useRef, useEffect } from "react";
import Avatar from "../Avatar/Avatar";
import MessageInputBlock from "../MessageInputBlock/MessageInputBlock";
import MessageItem from "../MessageItem/MessageItem";
import "./MessagesBlock.scss";

import searchImg from "../../../../static/photos/icons/search.png";
import optionsImg from "../../../../static/photos/icons/options.png";
import { useDispatch, useSelector } from "react-redux";
import { RootState } from "src/redux/store";
import renderMessagesSkeleton from "./helpers/renderMessagesSkeleton";
import {
  // fetchMessages,
  getCurrentDialog,
  sendNewMessage,
  setCurrentDialog,
} from "src/redux/actions";
import { sendMessage } from "src/api";
import { useNavigate } from "react-router-dom";
import ContentLoader from "react-content-loader";
import { usePosition } from "src/components/hooks/usePosition";

export default function MessagesBlock({ dialogId }) {
  const [inputBlockHeight, setInputBlockHeight] = useState("");
  const [messages, setMessages] = useState([]);
  const messagesBlockRef = useRef<any>();

  const user = useSelector((state: RootState) => state.user);
  const currentDialog = useSelector(
    (state: RootState) => state.chat.currentDialog
  );

  useEffect(() => {
    setMessages(currentDialog.messages);
  }, [currentDialog.messages]);

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const onChangeHeight = (height) => {
    setInputBlockHeight(`${height}px`);
  };

  useEffect(() => {
    // const roomName = JSON.parse(
    //   document.getElementById("room-name").textContent
    // );

    // const dialog = new URLSearchParams(window.location.search).get("dialog");

    // const url = window.location.href;
    // const dialog = url.split("/").reverse()[0];

    document.getElementById("room-name").textContent = dialogId;

    const chatSocket = new WebSocket(
      "ws://" + window.location.host + "/ws/my_messages/" + dialogId + "/"
    );

    chatSocket.onmessage = function (e) {
      const data = JSON.parse(e.data);
      console.log("data from socket", data);
      setMessages((oldArray) => [
        ...oldArray,
        {
          message_content: data.message_content,
          author_id: data.author_id,
          sent_date: data.sent_date,
        },
      ]);
      console.log("NEW MESSAGE: ", data.message);
    };

    chatSocket.onclose = function (e) {
      console.error("Chat socket closed unexpectedly");
    };

    document
      // .querySelector(".message-input__btn.send-btn")
      .addEventListener("onSendMessage", async () => {
        console.log("clicked send");
        const currentUser = document
          .querySelector("#user-name")
          .innerHTML.replace(/[\"]/g, "");
        const messageInputDom = document.querySelector(
          ".message-input"
        ) as HTMLInputElement;
        const message = messageInputDom.value;

        const body = {
          message_content: message,
          author_id: user.id,
          dialog_id: dialogId,
        };
        // dispatch(sendNewMessage(body));
        const { success } = await sendMessage(body);
        console.log("success?", success);
        if (success)
          chatSocket.send(
            JSON.stringify({
              message_content: message,
              author_id: user.id,
            })
          );
      });
  }, [dialogId]);

  useEffect(() => {
    if (messagesBlockRef.current) {
      messagesBlockRef.current.scrollTo(
        0,
        messagesBlockRef.current.scrollHeight
      );
    }
  }, [messages]);

  // useEffect(() => {
  //   const url = window.location.href;
  //   let dialog;

  //   if (url[url.length - 1] === "/") dialog = url.split("/").reverse()[1];
  //   else dialog = url.split("/").reverse()[0];

  //   console.log("DIALOGGG: ", dialog);
  //   if (!currentDialog.companion) dispatch(setCurrentDialogById(dialog));
  // }, []);

  // useEffect(() => {
  //   navigate('/my_messages')
  // }, [])

  useEffect(() => {
    console.log("messagesBlock");
    dispatch(getCurrentDialog(dialogId));
    // dispatch(setCurrentDialogById(dialogId));
    // dispatch(fetchMessages(dialogId));
  }, [dialogId]);

  const position = usePosition();

  console.log("POSITION", position);

  function renderMessages() {
    return (messages || []).map((item, index) => {
      const isMy = item.author_id === user.id;
      // const isWithAvatar = (i >0) ? messages[i-1].author_id
      let isWithAvatar = true;
      if (index > 0 && messages[index + 1]) {
        if (
          messages[index - 1].author_id !== item.author_id &&
          messages[index + 1].author_id === item.author_id
        )
          isWithAvatar = false;
        if (
          messages[index - 1].author_id === item.author_id &&
          messages[index + 1].author_id === item.author_id
        )
          isWithAvatar = false;
        if (
          messages[index - 1].author_id === item.author_id &&
          messages[index + 1].author_id !== item.author_id
        )
          isWithAvatar = true;
      } else isWithAvatar = true;

      const isFirst = index === 0;
      return (
        <MessageItem
          text={item.message_content}
          isMy={isMy}
          isOnline={false}
          isRead
          key={index}
          author={
            isMy ? `${user.name} ${user.surname}` : currentDialog.companion
          }
          date={item.sent_date}
          isWithAvatar={isWithAvatar}
          isFirst={isFirst}
        />
      );
    });
  }

  return (
    <div className="chat__main-block">
      <div className="chat__messages-block-header">
        {currentDialog.companion && !currentDialog.isLoading ? (
          <div className="chat__interlocutor">
            <Avatar
              width={40}
              height={40}
              isOnline={false}
              letter={currentDialog.companion[0]}
            />
            <div className="chat__interlocutor-info">
              <div className="chat__interlocutor-fullname">
                {currentDialog.companion}
              </div>
              <div className="chat__interlocutor-isonline">Онлайн</div>
            </div>
          </div>
        ) : (
          <ContentLoader
            speed={2}
            width={220}
            height={42}
            viewBox="0 0 220 42"
            backgroundColor="#efebeb"
            foregroundColor="#fafafa"
          >
            <circle cx="20" cy="20" r="20" />
            <rect x="55" y="1" rx="5" ry="5" width="160" height="12" />
            <rect x="55" y="25" rx="5" ry="5" width="100" height="12" />
          </ContentLoader>
        )}
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
        <div className="chat__messages-block" ref={messagesBlockRef}>
          {currentDialog.isLoading
            ? renderMessagesSkeleton()
            : renderMessages()}
        </div>
      </div>
      <div className="chat__input-block">
        <MessageInputBlock onChangeHeight={onChangeHeight} />
      </div>
    </div>
  );
}

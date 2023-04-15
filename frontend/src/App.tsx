import React, { useEffect } from "react";
import { render } from "react-dom";
import { useDispatch } from "react-redux";
import { Routes, Route } from "react-router-dom";

import { Home, Chat, Map } from "./components";
import { onLoad } from "./redux/actions";

import { blockHeightCalc } from "./utils";

export default function App() {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(onLoad());
  }, []);

  return (
    <div className="wrapper">
      <div className="content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/my_messages" element={<Chat />} />
          <Route path="/my_messages/:dialogId" element={<Chat />} />
          <Route
            path="/my_messages/new_dialog/:newDialogId"
            element={<Chat />}
          />
        </Routes>
      </div>
    </div>
  );
}

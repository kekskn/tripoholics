import React from "react";
import { render } from "react-dom";
import { Routes, Route } from "react-router-dom";

import { Home, Chat } from "./components";

import { blockHeightCalc } from "./utils";

export default function App() {
  return (
    <div className="wrapper">
      {/* <Header /> */}
      <div
        className="content"
        // style={{ marginTop: `${blockHeightCalc("nav")}px` }}
      >
        <Routes>
          {/* <Route path="*" element={<Home items={pizzas}/>}/> */}
          {/* <Route path="*" element={<Home items={this.props.items} />} /> */}
          <Route path="/" element={<Home />} />
          {/* <Route path="/my_messages" element={<Chat />} /> */}
          <Route path="/my_messages/*" element={<Chat />} />
        </Routes>
      </div>
    </div>
  );
}

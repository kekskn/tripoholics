import React from "react";
import ContentLoader from "react-content-loader";

export default function renderSkeleton() {
  return new Array(10).fill(1).map((_, i) => (
    <ContentLoader
      key={i}
      speed={2}
      width={330}
      height={48}
      viewBox="0 0 330 48"
      backgroundColor="#ebebeb"
      foregroundColor="#fafafa"
      style={{ padding: "12px 15px", boxSizing: "content-box" }}
    >
      <rect x="63" y="6" rx="3" ry="3" width="100" height="13" />
      <circle cx="24" cy="24" r="24" />
      <rect x="63" y="30" rx="3" ry="3" width="248" height="11" />
    </ContentLoader>
  ));
}

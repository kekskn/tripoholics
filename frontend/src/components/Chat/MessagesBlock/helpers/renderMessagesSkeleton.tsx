import React from "react";
import ContentLoader from "react-content-loader";
import cn from "classnames";

function renderMessagesSkeleton() {
  return new Array(5).fill(1).map((_, i) =>
    i % 2 == 0 ? (
      <div className={cn("message-item isWithAvatar")} key={i}>
        <ContentLoader
          speed={2}
          width={400}
          height={96}
          viewBox="0 0 400 96"
          backgroundColor="#efebeb"
          foregroundColor="#fafafa"
        >
          <circle cx="20" cy="76" r="20" />
          <rect x="51" y="0" rx="15" ry="15" width="120" height="34" />
          <rect x="52" y="43" rx="15" ry="15" width="296" height="53" />
        </ContentLoader>
      </div>
    ) : (
      <div className={cn("message-item isWithAvatar", { my: true })} key={i}>
        <ContentLoader
          speed={2}
          width={400}
          height={96}
          viewBox="0 0 400 96"
          backgroundColor="#efebeb"
          foregroundColor="#fafafa"
        >
          <circle cx="380" cy="76" r="20" />
          <rect x="225" y="0" rx="15" ry="15" width="120" height="34" />
          <rect x="49" y="43" rx="15" ry="15" width="296" height="53" />
        </ContentLoader>
      </div>
    )
  );
}

export default renderMessagesSkeleton;

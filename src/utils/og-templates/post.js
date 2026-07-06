import satori from "satori";
import { SITE } from "@/config";
import loadGoogleFonts from "../loadGoogleFont";

export default async post => {
  const siteLabel = SITE.title.toUpperCase();
  const dateLabel = new Date(post.data.pubDatetime).toISOString().slice(0, 10);
  const hostLabel = new URL(SITE.website).hostname;

  return satori(
    {
      type: "div",
      props: {
        style: {
          background: "#ffffff",
          color: "#111111",
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          padding: "56px 64px",
          fontFamily: "Noto Serif TC",
        },
        children: [
          {
            type: "div",
            props: {
              style: { display: "flex", flexDirection: "column" },
              children: [
                {
                  type: "div",
                  props: {
                    style: {
                      height: "10px",
                      width: "100%",
                      background: "#111111",
                    },
                  },
                },
                {
                  type: "div",
                  props: {
                    style: {
                      display: "flex",
                      justifyContent: "space-between",
                      alignItems: "baseline",
                      marginTop: "22px",
                      fontFamily: "Noto Sans TC",
                      fontWeight: 700,
                      fontSize: 24,
                      letterSpacing: "3px",
                    },
                    children: [
                      { type: "span", props: { children: siteLabel } },
                      {
                        type: "span",
                        props: {
                          style: { color: "#c8371e" },
                          children: dateLabel,
                        },
                      },
                    ],
                  },
                },
              ],
            },
          },
          {
            type: "div",
            props: {
              style: {
                display: "flex",
                flexDirection: "column",
                flexGrow: 1,
                justifyContent: "center",
              },
              children: [
                {
                  type: "div",
                  props: {
                    style: {
                      width: "76px",
                      height: "14px",
                      background: "#c8371e",
                      marginBottom: "30px",
                    },
                  },
                },
                {
                  type: "p",
                  props: {
                    style: {
                      fontSize: 62,
                      fontWeight: 900,
                      lineHeight: 1.3,
                      margin: 0,
                      maxHeight: "330px",
                      overflow: "hidden",
                    },
                    children: post.data.title,
                  },
                },
              ],
            },
          },
          {
            type: "div",
            props: {
              style: { display: "flex", flexDirection: "column" },
              children: [
                {
                  type: "div",
                  props: {
                    style: {
                      height: "4px",
                      width: "100%",
                      background: "#111111",
                      marginBottom: "20px",
                    },
                  },
                },
                {
                  type: "div",
                  props: {
                    style: {
                      display: "flex",
                      justifyContent: "space-between",
                      alignItems: "baseline",
                      fontSize: 26,
                    },
                    children: [
                      {
                        type: "span",
                        props: {
                          children: [
                            "by ",
                            {
                              type: "span",
                              props: {
                                style: {
                                  fontWeight: 700,
                                  marginLeft: "10px",
                                },
                                children: post.data.author,
                              },
                            },
                          ],
                        },
                      },
                      {
                        type: "span",
                        props: {
                          style: {
                            fontFamily: "Noto Sans TC",
                            fontWeight: 700,
                            fontSize: 22,
                            letterSpacing: "2px",
                          },
                          children: hostLabel,
                        },
                      },
                    ],
                  },
                },
              ],
            },
          },
        ],
      },
    },
    {
      width: 1200,
      height: 630,
      embedFont: true,
      fonts: await loadGoogleFonts(
        post.data.title +
          post.data.author +
          SITE.title +
          siteLabel +
          dateLabel +
          hostLabel +
          "by 0123456789-"
      ),
    }
  );
};

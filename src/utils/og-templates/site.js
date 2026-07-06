import satori from "satori";
import { SITE } from "@/config";
import loadGoogleFonts from "../loadGoogleFont";

export default async () => {
  const hostLabel = new URL(SITE.website).hostname;
  const kicker = "BLOG";

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
                      { type: "span", props: { children: kicker } },
                      {
                        type: "span",
                        props: {
                          style: { color: "#c8371e" },
                          children: hostLabel,
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
                      fontSize: 76,
                      fontWeight: 900,
                      lineHeight: 1.2,
                      margin: 0,
                    },
                    children: SITE.title,
                  },
                },
                {
                  type: "p",
                  props: {
                    style: {
                      fontSize: 28,
                      lineHeight: 1.6,
                      marginTop: "28px",
                      maxHeight: "140px",
                      overflow: "hidden",
                      color: "#444444",
                    },
                    children: SITE.desc,
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
                      justifyContent: "flex-end",
                      fontSize: 26,
                      fontWeight: 700,
                    },
                    children: {
                      type: "span",
                      props: { children: SITE.author },
                    },
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
        SITE.title + SITE.desc + SITE.author + hostLabel + kicker
      ),
    }
  );
};

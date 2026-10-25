# 示範影片（HTML 動畫轉 mp4）

做法：頁面定義 `window.render(t)`（t 為秒，依時間畫出該瞬間的畫面，純函式、無計時器），`cdp.mjs` 用 headless Chrome 逐格截圖，ffmpeg 合成。`example-demo.html` 是 work-mode 那支 27 秒影片的原始檔（版面 1280×720，樣式沿用 `../base.css`）。
```
D=$(mktemp -d); mkdir -p $D/frames          # 影格放暫存夾，不要放進 repo
node cdp.mjs "file://$PWD/example-demo.html" $D/frames $D/prof 27 12      # 27 秒、12 fps
ffmpeg -y -loglevel error -framerate 12 -i $D/frames/f%04d.png -vf "fps=24,format=yuv420p" -c:v libx264 -crf 22 -preset slow -movflags +faststart demo.mp4
ffmpeg -y -loglevel error -i $D/frames/f0144.png -q:v 3 demo-poster.jpg    # 海報取一格
```
規格：≤30 秒、<1MB（範例 239KB）；mp4 與 poster 放 `public/assets/posts/<basename>/`。換成新題目時改 `example-demo.html` 的文案與時間軸即可。

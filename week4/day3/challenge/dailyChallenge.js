// 🌟 Video Class Definition
class Video {
  constructor(title, uploader, time) {
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  }

  watch() {
    console.log(`${this.uploader} watched all ${this.time} seconds of "${this.title}"!`);
  }
}

// ✅ Create two video instances
const video1 = new Video("JavaScript OOP Basics", "Alice", 300);
const video2 = new Video("CSS Grid Tutorial", "Bob", 420);

video1.watch();
video2.watch();

// 🌟 Bonus: Array of video data
const videoData = [
  { title: "Intro to HTML", uploader: "Charlie", time: 200 },
  { title: "React Hooks Crash Course", uploader: "Dana", time: 600 },
  { title: "Node.js Server Basics", uploader: "Eve", time: 480 },
  { title: "Python for Beginners", uploader: "Frank", time: 540 },
  { title: "Git & GitHub Guide", uploader: "Grace", time: 360 }
];

// ✅ Loop through data and create instances
const videoInstances = videoData.map(data => new Video(data.title, data.uploader, data.time));

// ✅ Call watch() for each video
videoInstances.forEach(video => video.watch());

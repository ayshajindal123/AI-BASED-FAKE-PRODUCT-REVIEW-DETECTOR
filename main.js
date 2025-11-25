// main.js - fixed analyze() and download flow

async function analyze() {
    if (!localStorage.getItem("loggedIn")) {
        window.location.href = "login.html";
        return;
    }

    const url = document.getElementById("urlInput").value.trim();
    const errorText = document.getElementById("errorText");
    if (!url) {
        errorText.textContent = "Please enter a product URL.";
        return;
    }
    errorText.textContent = "";

    try {
        const res = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url })
        });

        if (!res.ok) {
            const txt = await res.text();
            errorText.textContent = "Backend error — cannot analyze. " + txt;
            return;
        }

        const data = await res.json();
        window.finalResult = data;

        document.getElementById("resultSection").classList.remove("hidden");
        document.getElementById("scoreText").textContent = data.trust_score + "%";
        document.getElementById("grade").textContent = data.grade;
        document.getElementById("verdict").textContent = data.verdict;
        // update circle (if present)
        const arc = document.getElementById("scoreArc");
        if (arc) arc.setAttribute("stroke-dasharray", `${data.trust_score},100`);

        // insights and reviews
        document.getElementById("insightList").innerHTML =
            data.insights.map(i => `<li>${i}</li>`).join("");

        document.getElementById("reviewList").innerHTML =
            data.reviews.map(r =>
                `<div class="review-card">${r.fake ? "❌ Fake" : "✔ Real"} — ${r.text}</div>`
            ).join("");

    } catch (err) {
        console.error("Analyze error:", err);
        errorText.textContent = "Failed to analyze — check server console.";
    }
}


document.getElementById("downloadPdfBtn").onclick = async () => {
    if (!window.finalResult) {
        alert("Analyze first.");
        return;
    }

    try {
        const res = await fetch("http://127.0.0.1:5000/download-pdf", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ result: window.finalResult })
        });

        if (!res.ok) {
            const txt = await res.text();
            alert("PDF error: " + txt);
            return;
        }

        const blob = await res.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        // try to read content-disposition fallback
        a.download = "FakeFind_Report.pdf";
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);
    } catch (err) {
        console.error("PDF download error:", err);
        alert("PDF download failed. Check server console.");
    }
};

// small helper for logout
function logout() {
    localStorage.removeItem("loggedIn");
    window.location.href = "login.html";
}

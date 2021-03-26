var theForm = document.forms["TDForm"];

var time_length = new Array();
time_length["none"] = 0;
time_length["Length"] = 1.00;

var style = new Array();
style["none"] = 0;
style["CleanVerbatim"] = 0;
style["Verbatim"] = 0.15;

var numberOfSpeakers = new Array();
numberOfSpeakers["none"] = 0;
numberOfSpeakers["1"] = 0;
numberOfSpeakers["2"] = 0;
numberOfSpeakers["3"] = 0.05;
numberOfSpeakers["4"] = 0.1;
numberOfSpeakers["10"] = 0.15;


var timestamps = new Array();
timestamps["none"] = 0;
timestamps["None"] = 0;
timestamps["SpeakerChange"] = 0.15;
timestamps["2Minutes"] = 0.15;


var turnAroundTime = new Array();
turnAroundTime["none"] = 0;
turnAroundTime["24"] = 0.35;
turnAroundTime["48"] = 0.15;
turnAroundTime["Standard"] = 0;


var audioQuality = new Array();
audioQuality["none"] = 0;
audioQuality["Bad"] = 0.1;
audioQuality["Fair"] = 0.05;
audioQuality["Good"] = 0;

function getTime_lengthPrice() {
    var default_price = 0;
    var theForm = document.forms["TDForm"];
    var selectedTime_length = theForm.elements["time_length"];
    time_lengthPrice = time_length[selectedTime_length.value] || default_price;
    return time_lengthPrice;
}

function getStylePrice() {
    var default_price = 0;
    var theForm = document.forms["TDForm"];
    var selectedStyle = theForm.elements["style"];
    stylePrice = style[selectedStyle.value] || default_price;
    return stylePrice
}

function getNumSpeakerPrice() {
    var default_price = 0;
    var theForm = document.forms["TDForm"];
    var selectedNumSpeaker = theForm.elements["number_of_speakers"];
    numSpeakerPrice = numberOfSpeakers[selectedNumSpeaker.value] || default_price;
    return numSpeakerPrice
}

function getTimeStampPrice() {
    var default_price = 0;
    var theForm = document.forms["TDForm"];
    var selectedTimeStamp = theForm.elements["timestamps"];
    timeStampPrice = timestamps[selectedTimeStamp.value] || default_price;
    return timeStampPrice
}

function getTatPrice() {
    var default_price = 0;
    var theForm = document.forms["TDForm"];
    var selectedTAT = theForm.elements["turn_around_time"];
    tatPrice = turnAroundTime[selectedTAT.value] || default_price;
    return tatPrice
}

function getAudioQualPrice() {
    var default_price = 0;
    var theForm = document.forms["TDForm"];
    var selectedAudioQual = theForm.elements["audio-quality"];
    audioQualPrice = audioQuality[selectedAudioQual.value] || default_price;
    return audioQualPrice
}

function getMinutes() {

    var timeContent = document.getElementById('total-time');
    var test = timeContent.textContent;
    console.log("text Content:" + test);
    var totalTime = parseInt(timeContent.textContent);
    return totalTime
}

function calculateTotal() {
    console.log("Time_length:" + getTime_lengthPrice());
    console.log("NumSpeaker:" + getNumSpeakerPrice());
    console.log("AudioQual:" + getAudioQualPrice());
    console.log("TAT:" + getTatPrice());
    console.log("Style:" + getStylePrice());
    console.log("TimeSt:" + getTimeStampPrice());
    console.log("Minutes:" + getMinutes() + " and type:" + typeof getMinutes());

    var multiplier = parseFloat(getTime_lengthPrice()) + parseFloat(getNumSpeakerPrice()) + parseFloat(getAudioQualPrice()) + parseFloat(getTatPrice()) + parseFloat(getStylePrice()) + parseFloat(getTimeStampPrice());
    console.log("Multiplier: " + multiplier.toFixed(2));

    var total = parseFloat(getMinutes()) * parseFloat(multiplier);
    console.log("Total:" + total.toFixed(2));

    console.log("**********************************************");

    document.getElementById('minuteCost').innerHTML =
        String(multiplier.toFixed(2));

    document.getElementById('total-cost').style.display='block';
        document.getElementById('totalCost').innerHTML =
            String(total.toFixed(2))
}




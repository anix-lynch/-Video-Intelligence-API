from dotenv import load_dotenv
from google.cloud import videointelligence

def load_video_content(file_path):
    with open(file_path, 'rb') as media_file:
        return media_file.read()
    
def config_speech_transcription(
        language_code='en-US', 
        punctuation=True, 
        profanity=False, 
        speaker_diarization=True, 
        speaker_count=2
    ):
    config = videointelligence.SpeechTranscriptionConfig(
        language_code=language_code,
        enable_automatic_punctuation=punctuation,
        filter_profanity=profanity,
        enable_speaker_diarization=speaker_diarization,
        diarization_speaker_count=speaker_count
    )
    return videointelligence.VideoContext(speech_transcription_config=config)

def process_video(video_client, input_content, context):
    operation = video_client.annotate_video(
        request={
            "features": [videointelligence.Feature.SPEECH_TRANSCRIPTION],
            "input_content": input_content,
            "video_context": context,
        }
    )
    print("\nProcessing video for speech transcription.")
    result = operation.result(timeout=600)
    print("\nFinished processing.\n")
    return result.annotation_results[0]

def print_transcription_result(transcription_result):
    for i, speech_transcription in enumerate(transcription_result.speech_transcriptions):
        for alternative in speech_transcription.alternatives:
            print("Alternative level information:")
            print('from result {}'.format(i))
            print("Transcript: {}".format(alternative.transcript))
            print("Confidence: {}\n".format(alternative.confidence))

            print("Word level information:")
            for word in alternative.words:
                print(
                    "Speaker Tag: {}, \nWord: {}, start_time: {}, end_time: {}".format(
                        word.speaker_tag, word.word, word.start_time, word.end_time
                    )
                )

def main():
    load_dotenv()
    input_content = load_video_content('./resource/job_mock_interview.mp4')
    video_client = videointelligence.VideoIntelligenceServiceClient()
    context = config_speech_transcription()
    annotation_result = process_video(video_client, input_content, context)
    print_transcription_result(annotation_result)

main()

from dotenv import load_dotenv
from google.cloud import videointelligence

def load_video_content(file_path):
    with open(file_path, 'rb') as media_file:
        return media_file.read()
    
def process_video(video_client, input_content):
    operation = video_client.annotate_video(
        request={
            "features": [videointelligence.Feature.TEXT_DETECTION],
            "input_content": input_content,
        }
    )
    print("\nProcessing video for text detection.")
    result = operation.result(timeout=300)
    print("\nFinished processing.\n")
    return result.annotation_results[0]

def print_text_detection_annotations(annotation_result):
    for text_annotation in annotation_result.text_annotations:
        print("\nText: {0}".format(text_annotation.text))

        text_segment = text_annotation.segments[0]
        start_time = text_segment.segment.start_time_offset
        end_time = text_segment.segment.end_time_offset
        print(
            "start_time: {0}, end_time: {1}".format(
                start_time.seconds + start_time.microseconds * 1e-6,
                end_time.seconds + end_time.microseconds * 1e-6,
            )
        )

        print("Confidence: {0}".format(text_segment.confidence))

def main():
    load_dotenv()
    input_content = load_video_content('./resource/7842850-hd_1080_1920_30fps.mp4')
    video_client = videointelligence.VideoIntelligenceServiceClient()
    annotation_result = process_video(video_client, input_content)
    print_text_detection_annotations(annotation_result)

main()
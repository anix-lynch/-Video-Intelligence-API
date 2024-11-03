from dotenv import load_dotenv
from google.cloud import videointelligence

def load_video_content(file_path):
    with open(file_path, 'rb') as media_file:
        return media_file.read()
    
def process_video(video_client, input_content):
    operation = video_client.annotate_video(
        request={
            "features": [videointelligence.Feature.LOGO_RECOGNITION],
            "input_content": input_content,
        }
    )
    print("\nProcessing video for logo detection annotations.")
    result = operation.result(timeout=300)
    print("\nFinished processing.\n")
    return result.annotation_results[0]

def print_logo_detection_annotations(annotation_result):
    for logo_recognition_annotation in annotation_result.logo_recognition_annotations:
        entity = logo_recognition_annotation.entity
        print("Entity Id : {}".format(entity.entity_id))
        print("Description : {}".format(entity.description))

        for track in logo_recognition_annotation.tracks:
            # Video segment of a track.
            print(
                "\n\tStart Time Offset : {0}.{1}".format(
                    track.segment.start_time_offset.seconds,
                    track.segment.start_time_offset.microseconds * 1000,
                )
            )
            print(
                "\tEnd Time Offset : {0}.{1}".format(
                    track.segment.end_time_offset.seconds,
                    track.segment.end_time_offset.microseconds * 1000,
                )
            )
            print("\tConfidence : {0}".format(track.confidence))

def main():
    load_dotenv()
    input_content = load_video_content('./resource/4062021-hd_1920_1080_30fps.mp4')
    video_client = videointelligence.VideoIntelligenceServiceClient()
    annotation_result = process_video(video_client, input_content)
    print_logo_detection_annotations(annotation_result)

main()
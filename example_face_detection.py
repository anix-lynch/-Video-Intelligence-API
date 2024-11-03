from dotenv import load_dotenv
from google.cloud import videointelligence

def load_video_content(file_path):
    with open(file_path, 'rb') as media_file:
        return media_file.read()
    
def configure_face_detection(include_bounding_boxes=False, include_attributes=True):
    config = videointelligence.FaceDetectionConfig(
        include_bounding_boxes=include_bounding_boxes,
        include_attributes=include_attributes
    )
    return videointelligence.VideoContext(face_detection_config=config)

def process_video(video_client, input_content, context):
    operation = video_client.annotate_video(
        request={
            "features": [videointelligence.Feature.FACE_DETECTION],
            "input_content": input_content,
            "video_context": context,
        }
    )
    print("\nProcessing video for face detection annotations.")
    result = operation.result(timeout=300)
    print("\nFinished processing.\n")
    return result.annotation_results[0]

def print_face_detection_annotations(annotation_result):
    for annotation in annotation_result.face_detection_annotations:
        print("Face detected:")
        for track in annotation.tracks:
            print(
                "Segment: {0}s to {1}s".format(
                    track.segment.start_time_offset.seconds
                    + track.segment.start_time_offset.microseconds / 1e6,
                    track.segment.end_time_offset.seconds
                    + track.segment.end_time_offset.microseconds / 1e6,
                )
            )

            timestamped_object = track.timestamped_objects[0]

            # Return attributes if available
            # Attributes include glasses, headwear, smiling, direction of gaze, etc
            print("Attributes:")
            for attribute in timestamped_object.attributes:
                print(
                    "\t{0}:{1} {2}".format(
                        attribute.name, attribute.value, attribute.confidence
                    )
                )

def main():
    load_dotenv()
    input_content = load_video_content('./resource/854204-hd_1280_720_30fps.mp4')
    video_client = videointelligence.VideoIntelligenceServiceClient()
    context = configure_face_detection()
    annotation_result = process_video(video_client, input_content, context)
    print_face_detection_annotations(annotation_result)

main()
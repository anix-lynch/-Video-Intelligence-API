from dotenv import load_dotenv
from google.cloud import videointelligence

def load_video_content(file_path):
    with open(file_path, 'rb') as media_file:
        return media_file.read()
    
def configure_people_detection(
        include_bounding_boxes=False, 
        include_attributes=True, 
        include_pose_landmarks=True
    ):
    config = videointelligence.PersonDetectionConfig(
        include_bounding_boxes=include_bounding_boxes,
        include_attributes=include_attributes,
        include_pose_landmarks=include_pose_landmarks

    )
    return videointelligence.VideoContext(person_detection_config=config)

def process_video(video_client, input_content, context):
    operation = video_client.annotate_video(
        request={
            "features": [videointelligence.Feature.PERSON_DETECTION],
            "input_content": input_content,
            "video_context": context,
        }
    )
    print("\nProcessing video for people detection annotations.")
    result = operation.result(timeout=300)
    print("\nFinished processing.\n")
    return result.annotation_results[0]

def print_people_detection_annotations(annotation_result):
    for person in annotation_result.person_detection_annotations:
        print("Person detected:")
        for track in person.tracks:
            print(
                "Segment: {0}s to {1}s".format(
                    track.segment.start_time_offset.seconds
                    + track.segment.start_time_offset.microseconds / 1e6,
                    track.segment.end_time_offset.seconds
                    + track.segment.end_time_offset.microseconds / 1e6,
                )
            )

            if track.timestamped_objects:
                timestamped_object = track.timestamped_objects[0]

                # Return attributes if available
                print("Attributes:")
                for attribute in timestamped_object.attributes:
                    print(
                        "\t{0}:{1} {2}".format(
                            attribute.name, attribute.value, attribute.confidence
                        )
                    )

                print("Landmarks:")
                for landmark in timestamped_object.landmarks:
                    print(
                        "\t{0}: {1} (x={2}, y={3})".format(
                            landmark.name,
                            landmark.confidence,
                            landmark.point.x,
                            landmark.point.y,
                        )
                    )

def main():
    load_dotenv()
    input_content = load_video_content('./resource/nightmarket.mp4')
    video_client = videointelligence.VideoIntelligenceServiceClient()
    context = configure_people_detection()
    annotation_result = process_video(video_client, input_content, context)
    print_people_detection_annotations(annotation_result)

main()
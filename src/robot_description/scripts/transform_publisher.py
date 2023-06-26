#!/usr/bin/python3
import rospy
import tf2_ros
import geometry_msgs.msg

rospy.init_node('transform_publisher')

tf_broadcaster = tf2_ros.TransformBroadcaster()

while not rospy.is_shutdown():
    transform = geometry_msgs.msg.TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = 'odom'
    transform.child_frame_id = 'laser_frame'
    transform.transform.translation.x = 0.0  # Ingresar los valores de la transformación deseada
    transform.transform.translation.y = 0.0
    transform.transform.translation.z = 0.0
    transform.transform.rotation.x = 0.0
    transform.transform.rotation.y = 0.0
    transform.transform.rotation.z = 0.0
    transform.transform.rotation.w = 1.0

    tf_broadcaster.sendTransform(transform)

    rospy.sleep(0.1)  # Esperar un intervalo de tiempo antes de publicar la siguiente transformación

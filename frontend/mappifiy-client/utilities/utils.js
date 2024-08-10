
const SERVER_IP = '192.168.138.115'

export function getServerIp(){
    return SERVER_IP 
}
export function getSmartPhoneFps(){
    // May be replaced in the future if 
    // quering the device is possible
    STANDARD_SMARTPHONE_FPS = 30
    return STANDARD_SMARTPHONE_FPS
}


export function getBaseUrl(){
    return `http://${getServerIp()}:8000`
} 
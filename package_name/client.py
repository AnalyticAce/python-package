"""
Main client for {PACKAGE_DISPLAY_NAME}.
"""

import requests
from typing import Optional, Dict, Any

from .config import Config, default_config
from .exceptions import APIError, AuthenticationError


class Client:
    """Main client class for {PACKAGE_DISPLAY_NAME}."""
    
    def __init__(self, config: Optional[Config] = None):
        """
        Initialize the client.
        
        Args:
            config: Configuration object. If None, uses default config.
        """
        self.config = config or default_config
        self.session = requests.Session()
        
        # Set up default headers
        self.session.headers.update({
            "User-Agent": f"{{PACKAGE_NAME}}/{self.get_version()}",
            "Content-Type": "application/json",
        })
        
        if self.config.api_key:
            self.session.headers["Authorization"] = f"Bearer {self.config.api_key}"
    
    def get_version(self) -> str:
        """Get the package version."""
        try:
            from . import __version__
            return __version__
        except ImportError:
            return "unknown"
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Make an HTTP request to the API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            **kwargs: Additional arguments for requests
            
        Returns:
            Response data as dictionary
            
        Raises:
            APIError: If the request fails
            AuthenticationError: If authentication fails
        """
        url = f"{self.config.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=self.config.timeout,
                **kwargs
            )
            
            if response.status_code == 401:
                raise AuthenticationError("Authentication failed")
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise APIError(f"Request failed: {e}") from e
    
    def get_data(self, resource_id: str) -> Dict[str, Any]:
        """
        Example method to get data from the API.
        
        Args:
            resource_id: ID of the resource to retrieve
            
        Returns:
            Resource data
        """
        return self._make_request("GET", f"/data/{resource_id}")
    
    def create_resource(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Example method to create a resource.
        
        Args:
            data: Resource data to create
            
        Returns:
            Created resource data
        """
        return self._make_request("POST", "/data", json=data)